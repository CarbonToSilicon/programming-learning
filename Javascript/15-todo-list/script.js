// const todolist = {};
const tasksList = [];
const datesList = [];

function addTodo() {
    let todoName = document.querySelector(".text1");
    let todoDate = document.querySelector('.date1');
    
    // 1. Validate if fields are filled out first
    if (todoName.value.trim() === "") {
        alert("Please type a task!");
        return;
    }
    if (todoDate.value === "") {
        alert("Please select a valid date!");
        return;
    }
    
    // 2. Safely push the values into your arrays
    tasksList.push(todoName.value);
    datesList.push(todoDate.value);
    
    console.log("Tasks:", tasksList);
    console.log("Dates:", datesList);

    // 3. Reset form inputs safely AFTER values are stored
    todoName.value = "";
    todoDate.value = "";
}
//-------------------------------------------
