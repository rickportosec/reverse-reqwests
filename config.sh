#!/bin/bash

while [[ $# -gt 0 ]]
do
setup="$1"

case $setup in
    --windows)
    sed -i 's/    return cmd/    ps = f"powershell {cmd}"\n    return ps/' svflask.py
    sed -i '37 s/0/1/; 39 s/1/2/' src/main.rs
    ;;
    --unix)
    sed -i '/    ps = f"powershell {cmd}"/d' svflask.py
    sed -i 's/    return ps/    return cmd/' svflask.py
    sed -i '37 s/1/2/; 39 s/0/1/' src/main.rs
    ;;
    --addr)
    new_addr="$2"
    sed -i "s/addr=\".*\"/addr=\"$new_addr\"/" svflask.py
    sed -i "s/static IP_ADDR: \&str = \".*\"/static IP_ADDR: \&str = \"$new_addr\"/" src/main.rs
    ;;
    --port)
    new_port="$2"
    sed -i "s/port=.*/port=$new_port/" svflask.py
    sed -i "s/static PORT: u32 = .*/static PORT: u32 = $new_port;/" src/main.rs
    ;;
    --proto)
    new_proto="$2"
    sed -i "s/static PROTO: \&str = \".*\"/static PROTO: \&str = \"$new_proto\"/" src/main.rs
    ;;
    *)
    ;;

esac
shift
done
