## Command Mode

- `:jumps`: lookup history of jumplist

- `:marks`: lookup all marks

- `:changes`: lookup all history all positions changed 

- `:register`: list register

- replace all words:
~~~
:%s/target/replacement/g
~~~


## Normal Mode

### Jump

- `ctrl-o`: go to older cursor position in jumplist
- `ctrl-i`: go to newer cursor position in jumplist
- `''`: go to position before latest jump
- `gi`: insert text in the same position as where Insert mode was stoped last time
- ``.`: location of last change
- ``^`: location of last change
- ``[`: start of last change or yank
- `g;`: traverse backward change list
- `g,`: traverse forward change list

### Edit

- `"0p`: paste content yanked last


### Search

- `/\v`: for regex search

### Folding

- `zf`: folding lines
- `zo`: unfolding 


## Insert mode

- `ctrl-r0`: paste content yanked last

- `<ctrl>-a (or <ctrl><sapce>)`: insert previously inserted text


## Visual Mode

- `gv`: Start Visual mode with the same area as the previous area and the same mode.


## Others

- check out what's changed compared to original file
~~~
:w !diff % -
~~~

