// donmt judge me for this,,, i just might as well write all this down
// i remember things better when i write it down anyway, not that i wont remember most of this

// this is also not guaranteed to compile

fn main() {
  // weird syntax stuff
    let arr = [3;5] // [3,3,3,3,3]
    let secret = rand::thread_rng().gen_range(1..101); // start is inclusive, end is exclusive
    let secret = rand::thread_rng().gen_range(1..=101); // above but end is inclusive


  // data types ig
    // integer overflow is a thing, so, you know, select a number thing thatll work for u
    // i32 is the default, when type is not specified
    let c: u32 = 100 // creates 32-bit unsigned integer 
    // can also be: i8,i16,i32,i64,i128,isize, u8,u16,u32,u64,u128,usize
    // "u" means unsigned, aka has to be positive. "i" means signed, aka can be either
    // isize and usize are based on architecture of cpu: 64-bits or 32-bits

    // booleans also exist, also very obviously
    let t = true;
    let f: bool = false;

    // characters also exist cuz y not 
    let c = 'z'; // they MUST use single quotes
    let z = 'ℤ';
    let heart_eyed_cat = '😻';

    // ,,,and tuples
    let tup: (i32, i32, i32) = (500, 6, 1);
    let (x,y,z) = tup; // destructure the whole tuple
    let x = tup.0;

    // ,,,,,,and arrays
    let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
    let arr: [i32;5] = [1,2,3,4,5];
    let arr2 = [3; 5]; // [3,3,3,3,3]
    let first = a[0];

  // functions n stuff
    fn add_nums(num1:i32,num2:i32) -> i32 {
        num1+num2 // returns - no semicolon
    }
    println!("Sum of 4 and 3 is: {}", add_nums(4,3))

  // flow n stuff
    if x < 5 {
        println!("condition was true");
    // else if x > 5 { do_stuff() };
    } else { // if you dont put else, the if condition is just skipped.. as expected
        println!("condition was false");
    }
    // save in variable based on if statement
    let number = if condition { 5 } else { 6 }; // if condition, number = 5; else, number = 6
    loop {
        // repeats this until `break`ed
        // (obviously continue also exists)
        if x == 10 {break;}
        x++
    }
    // break and continue work for the innermost loop.
    // if you need to specify,
    'name: loop {
        if x == 100 {
            // breaks the loop labelled 'name
            break 'name x // the "x" here specifies you want to be able to use the value out of the loop
        }
        x++
    }
    while condition { // works like normal
        do_stuff();
    }
    for element in a {
        do_stuff()
    }
    for x in (1..4).rev() { // .rev() reverses it. means 3,2,1 (as `..` is exclusive on the end)
        do_stuff()
    }

  // operations also exist obviously
    5+10;
    95.5-4.3;
    4*30;
    56.7/32.2;
    2/3; // results in 0, cuz theyre both integers, not floats
    43%5;

}