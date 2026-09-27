// 1. LOAD DATA PERMANENTLY ON PAGE LOAD
// We check if there are saved tasks. If yes, convert text back to an array. If not, start fresh [].
let tasksList = JSON.parse(localStorage.getItem("savedTasks")) || [];

// Run the render function immediately so existing tasks appear right away when opening the page
renderTodos();

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
    
    
    // Push a combined object into the array
    tasksList.push({
        id: Date.now(), // Unique ID to easily find and delete later
        name: todoName.value.trim(),
        datetime: todoDate.value, // e.g., "2026-10-04T14:30"
        completed: false // NEW STATE: All tasks start out unfinished!
    });
    
    console.log("TasksList:", tasksList);
    

    // 3. Reset form inputs safely AFTER values are stored
    todoName.value = "";
    todoDate.value = "";
  
    // Save the updated list to localStorage, then draw the screen
    saveToStorage();
    renderTodos();
}
//-------------------------------------------

// 2. NEW HELPER FUNCTION: Saves the current array into the browser memory
function saveToStorage() {
    // JSON.stringify turns our array of objects into a single long string of text
    localStorage.setItem("savedTasks", JSON.stringify(tasksList));
}

// NEW LOGIC: Toggles the completion state when a user clicks the checkbox
function toggleTodo(id) {
    for (let task of tasksList) {
        if (task.id === id) {
            task.completed = !task.completed; // Flips true to false, or false to true
            break;
        }
    }
    saveToStorage();
    renderTodos(); // Redraw the screen to apply or remove the strike-through
}

function renderTodos() {
    const container = document.querySelector(".all-tasks-container");
    container.innerHTML = "";
    if (tasksList.length === 0) return;

    // STEP A: Sort everything chronologically by date and time
    tasksList.sort((a, b) => new Date(a.datetime) - new Date(b.datetime));

    console.log(tasksList);
    const groups = {};

    tasksList.forEach(task => {
        // Extract just the Date part (YYYY-MM-DD) from the full timestamp
        const dateKey = task.datetime.split('T')[0]; 
        
        if (!groups[dateKey]) {
            groups[dateKey] = [];
        }
        groups[dateKey].push(task);
    });
    // STEP C: Loop through the grouped dates and render them to the screen
    // Object.keys(groups) gives us sorted date headers automatically
    Object.keys(groups).sort().forEach(date => {
        
        // 1. Create a container element for the group
        const groupContainer = document.createElement('div');
        groupContainer.className = 'date-group-wrapper';

        // 2. Format the date header (uses your .filtered-date class styling)
        // Formats "2026-10-04" into a friendlier look like "04/10/2026"
        const displayDate = date.split('-').reverse().join('/'); 
        let groupHTML = `<div class="filtered-date">${displayDate}</div>`;

        // 3. Loop through all the tasks belonging to this specific date
        groups[date].forEach(task => {
            // Extract just the time layout from the timestamp (HH:MM)
            const timeString = task.datetime.split('T')[1] || "";
          
            // NEW LOGIC: Check if this task is completed to keep the checkbox checked on refresh
            const isChecked = task.completed ? "checked" : "";
          
            groupHTML += `
                <div class="task-list">
                    <!-- Added onclick="toggleTodo(${task.id})" to trigger the switch -->
                    <input type="checkbox" class="tick-box" ${isChecked} onclick="toggleTodo(${task.id})">
                    
                    <!-- Added a condition to append the 'completed' class if task.completed is true -->
                    <div class="task-box taskBoxText ${task.completed ? 'completed' : ''}">
                        <span>${task.name}</span>
                        <small style="color: #6b7280; margin-left: 8px;">(${timeString})</small>
                    </div>
                    <button class="task-remove" onclick="deleteTodo(${task.id})"></button>
                </div>
            `;
        });
        groupContainer.innerHTML = groupHTML;
        container.appendChild(groupContainer);
    });
};

function deleteTodo(id) {
    tasksList = tasksList.filter(task => task.id !== id);
    saveToStorage(); // Save changes after deleting an item
    renderTodos();
}

// 3. NEW LOGIC: Clear all tasks at once
function clearAllTodos() {
    // Ask for user confirmation so they don't accidentally delete everything
    if (confirm("Are you absolutely sure you want to clear all tasks?")) {
        tasksList = []; // Empty out the main data array
        localStorage.removeItem("savedTasks"); // Wipe the entry out of browser storage
        renderTodos(); // Clear the screen
    }
}