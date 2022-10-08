use std::env;

fn validate(input){
    if input.contains(",") {
        input = input.split(",") 
    }
}

fn main() {
  let mut i= 0;
  let  y:i64 = 100000000000;
  let args: Vec<_> = env::args().collect();
   if args.len() > 1 {
    let mut start_number = args[1]
    let mut middle_number = args[2]
    let mut end_number = args[3]

    start_number = start_number.split(",") 
    middle_number = middle_number.split(",") 
    end_number = end_number.split(",") 


    }
  println!("done");
}   