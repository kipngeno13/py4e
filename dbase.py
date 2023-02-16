import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cursor = connection.cursor()
cursor.execute( 'DROP TABLE IF EXISTS Counts' )

cursor.execute('CREATE TABLE Counts (email TEXT,count INTEGER)')

fname = input('Enter file name : ')
try:
    fhandle = open(fname)
except:
    print('file could not be opened')
    quit()

for line in fhandle:
    if not line.startswith('From'): continue
    pieces = line.split()
    email = pieces[1]
    cursor.execute('SELECT count FROM Counts WHERE email = ?',(email,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (email,count) VALUES (?,1)',(email,))
    else:
        cursor.execute('UPDATE Counts SET count = count+1 WHERE email = ?',(email,))

record = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cursor.execute(record):
    print(str(row[0]),str(row[1]))