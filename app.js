function addTask(){

    let task =
    document.getElementById("task").value.toUpperCase();

    let li=document.createElement("li");

    li.innerHTML = task;

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
