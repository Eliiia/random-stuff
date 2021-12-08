// donmt judge me for this,,, i just might as well write all this down
// i remember things better when i write it down anyway, not that i wont remember most of this

// this is also not guaranteed to compile

// oh yeah and:
// this isnt intended to be easy to read as i probably am not expecting to read back through this without ctrl+f

// as of 08/12/2021: im just not gonna bother with the rest of this 

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

  // scopes n ownership n stuff
    // actual explanation here:
    // https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
    {
        let s = "hello" // (string literals are stored on the stack)
        // s is usable here, as expected
    } // s is not usable here, as expected

    // stores string on a heap, in case the value isnt known at compile time
    let mut s = String::from("hello") 
    s.push_str(", world!") // also means it can be mutable, unlike hardcoded strings

    // this thing is a bit weird yo
    // (ALL OF THE BELOW only applies to items on the heap, not on the stack - such as strings)
    let s1 = String::from("hello");
    // when we declare this, the string itself is stored on the heap
    // however, on the stack: the pointer, length, and capacity (allocated space on the heap) are stored  
    let s2 = s1; // so when we declare this, it uses the same pointer, going to the EXACT same data
    s2[0] = "y" // this would change both s1 and s2, as they both point to the same thing
    // s1 is no longer considered valid after `let s2 = s1` to stop them both from trying to invalidate
    // explained better here: https://doc.rust-lang.org/book/img/trpl04-02.svg
    let s2 = s1.clone(); // this line will instead "clone" it, causing them to point to seperate points of data
    // this is not a good thing to do, as it is very cpu and ram expensive

    // losing ownership
    let s = String::from("helloooooo") // this is in the heap, therefore:
    function(s) // s is no longer valid cuz it was "given" to the function
    let x = 5; // this is in the stack
    function(5); // therefore x still functions after this, as it is "copied", not "given" to the function

    // Borrowing ownership
    fn borrow(x: &i32) { 
        // (x: &mut i32) if we want it to be mutable
        // important limitation: can only have 1 mutable reference at a time
        x++
    }
    let /*mut*/ x = 0;
    borrow(&x); // or `borrow(&mut x)`
    x++; // doesnt throw an error, as x is still there, as it was only a reference
    // it was not passed to the function.
}
// stopped writing as of 08/12/2021