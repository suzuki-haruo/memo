
let x = 0;
console.log(x);
function onClick(){
	console.log('success');
	let template = document.getElementById("template");
	let task_input = document.getElementById("task_input");
	
	let task_value = template.getAttribute("value");

	task_input.value = task_value;


	
	
}

// function onSubmit(){
// 	template_input = document.getElementById("template_input");
// 	if(template_input.length = 0){
// 		console.log("empty");
// 		window.prompt("テンプレートが入力されていません。");
// 	}else{
// 		console.log("OK");
// 	}
// }

function onClick2(){
	document.getElementById("temp_del_button");
	let x=x-1;
}
function onClick3(){
	// document.getElementById("temp_button");
	// let x=x+1;
	template_input = document.getElementById("template_input");
	if(!str || template_input.length == 0){
		console.log("empty");
		window.prompt("テンプレートが入力されていません。");
	}else{
		console.log("OK");
	}
	
}
if(x>=2){
	window.alert("一番上のテンプレートのみが機能します。");
}else{
	console.log(x);
}

