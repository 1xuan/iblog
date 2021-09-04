Assume you have a file `show.py`.

There is an example.

~~~bash
_show_complete()
{
    local cur prev opts node_names
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts=`$show.py --help | grep '  --' | awk '{print $1}'`

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}

complete -F _show_complete show.py
~~~

- `COMP_WORDS`: A array of words which appear in cli
- `COMP_CWORD`: The Index of cursor
- `COMP_CWORD`: The Index of cursor
- `cur`: Word and the cursor

**Reference**

[Creating a bash completion script](https://iridakos.com/programming/2018/03/01/bash-programmable-completion-tutorial)

