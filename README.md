
## REVERSE-REQWESTS


____________________________________________________________________________________________________
### `Description`

Projeto criado com a ideia de executar comando arbitrário em computadores usando de intermédio um servidor web tunelado com ngrok.

A maquina comprometida entrará em loop infinito de requests. O get recebido no servidor ira spawnar um input resultando no client aguardando até que o conteúdo seja exibido no body da aplicação, após o return do comando no input a maquina irá executar o response e enviar o output para o servidor utilizando o metodo post.

____________________________________________________________________________________________________
### `Requeriments`

* `cargo` https://www.rust-lang.org/
* `git`  (clone esse repositorio)
* `pip` https://www.python.org/ (`pip3 install -r requeriments.txt`)
* `ngrok` https://ngrok.com/ (`sudo apt-get install libssl-dev`)
____________________________________________________________________________________________________
### `Server`
```
python3 svflask-ngrok.py
```
____________________________________________________________________________________________________
### `Build`
```
cargo b --release
```

____________________________________________________________________________________________________

😇 https://www.virustotal.com/gui/file/7c907e0079548e4adcc4d65480dcf1d4fecae18deb4fef96295a79ac127300df?nocache=1
