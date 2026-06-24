
function addTask() {

    let task = document.getElementById("task").value;

    let li = document.createElement("li");

    li.innerHTML = `
        <span onclick="completeTask(this)">
            ${task}
        </span>

        <button onclick="editTask(this)">
            Edit
        </button>
    `;

function addTask(){

    let task =
    document.getElementById("task").value.toUpperCase();

    let li=document.createElement("li");

    li.innerHTML = task;
feature/improve-task-display

    document.getElementById("list").appendChild(li);
}
}
function completeTask(task) {
    task.classList.toggle("completed");
}
function deleteTask(button) {
    button.parentElement.remove();
}
function clearTasks(){
    document.getElementById("list").innerHTML="";
}
function updateTaskCount() {
    const taskCount = document.querySelectorAll("#taskList li").length;
    console.log(`Total tasks: ${taskCount}`);
}
let selectedTask = null;


function editTask(button){

    selectedTask = button.parentElement;

    document.getElementById("editInput").value =
    selectedTask.innerText;

}
function saveEdit(){

    let newText =
    document.getElementById("editInput").value;

    selectedTask.firstChild.textContent = newText;
    if(newText.trim() === ""){
    alert("Task cannot be empty");
    return;
}

}