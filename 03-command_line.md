# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * cat -- show file contents (catalog)
> > * cp -- copy file(s) from one directory to another
> > * du -- calculates size of current directory
> > * echo -- takes input string as argument and prints it as output
> > * ls -- list directory contents
> > * ls -a -- list directory contents including hidden files
> > * ls -l -- list directory contents in long format
> > * ls -t -- list directory contents sorted by time last modified (recent first)  
> > *All the previous options can be combined, e.g. 'ls -alt'*  
> > * man -- show manual entry on a command
> > * mkdir -- create directory
> > * mv -- move file (or rename)
> > * pwd -- print working directory
> > * rm -- permanently remove (delete) a file
> > * rm -r -- permanently remove (delete) a directory and all of its contents
> > * touch -- creates a file

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * ls -- lists contents of working directory
> > * ls -a -- lists contents including hidden files
> > * ls -l -- lists contents in long form
> > * ls -lh -- lists contents in long form with readable file size
> > * ls -lah -- lists contents in long form, including hidden files, with readable file size
> > * ls -t -- lists files sorted by time last modified (recent first)
> > * ls -Glp -- list files in long form (-l) with slashes added behind directory names (-p) and colorized output enabled (-G)

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * ls -f -- output isn't sorted by type, only alphanumerically (automatically turns on -a)
> > * ls -m -- stream output format, which lists files across page separated by commas
> > * ls -R -- recursively list contents of any subdirectories
> > * ls -r -- reverse the sort order
> > * ls -S -- list files by size

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The 'xargs' command allows for multiple arguments to be provided to a single command. For example, if a user were trying to find several different file types in a directory:  
```console
$ xargs -n 1 find . -name
"*.md" "*.txt" "*.py"
```

 

