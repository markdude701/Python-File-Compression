# Python File Compression
## Create Tar & Tar.gz files

### Imports / Requirements:
- tarfile
- OS
- glob

### Sample Output
```
<<<<<<< HEAD
Collected Directory items: ['archive.tar', 'archive.tar.gz', 'bar', 'conversion.py', 'foo', 'quux', 'readme.md', 'venv']
=======
>>>>>>> 08e6514dfc0dedfa352a0126b720d6c5e9a39e91
Deleted old archive.tar
Deleted old archive.tar.gz
Collected Directory items: ['bar', 'conversion.py', 'foo', 'quux', 'readme.md', 'venv']
Created archive.tar
Created archive.tar.gz
Compression Complete!
Original Directory File Size: 28.0 MB
<<<<<<< HEAD
Tar File Size: 19.8 MB - Compression : 70.92981113181558 % 
Tar.gz File Size: 8.1 MB - Compression : 29.04161947711844 % 
=======
Tar File Size: 19.8 MB - Compression : 70.9327368819292 % 
Tar.gz File Size: 8.1 MB - Compression : 29.042098108628977 % 
['archive.tar', 'archive.tar.gz', 'bar', 'conversion.py', 'foo', 'quux', 'venv']
>>>>>>> 08e6514dfc0dedfa352a0126b720d6c5e9a39e91
```
