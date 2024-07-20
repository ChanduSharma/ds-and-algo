function main_var() {
	console.log("Hoisting example in case of var");
	console.log("In case it is not defined");
	console.log("value of ex ",ex);
	// expected: undefined , meaning it is declared but not defined
	// logging a not defined variable.
	try {
		console.log("Value of undeclared variable ", a);
	} catch(error) {
		// Since a is not even declared so we get "not defined"
		// instead of undefined.
		console.log("value of undeclared variable ",error.message);
	}
	ex = 5;
	console.log('value of ex after defined',ex);
	var ex;
	{
		// let b;
		console.log("Value of a let variable before it is defined");
		try {
			console.log("value of b ", b);
		} catch (err) {
            console.log("error ", err.message);
            // we get error of b not being initialized and not like undefined
            // so the interpreter knows that it is there, we just can't use it
            // before initializing the variable.
        }
   		let b;
        b = 5;
        console.log("Value of b variable after initialization ",b);
	}
}

main_var()
