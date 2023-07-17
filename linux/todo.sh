#!/bin/bash

# This script simulates a basic todo list

# Initialize an empty array to store tasks
tasks=()

# Function to add a task to the list
add_task() {
  local task=$1
  tasks+=("$task")
  echo "Task added: $task"
}

# Function to view the list of tasks
view_tasks() {
  if [ ${#tasks[@]} -eq 0 ]; then
    echo "No tasks found. Your todo list is empty."
  else
    echo "Todo List:"
    for ((i = 0; i < ${#tasks[@]}; i++)); do
      echo "$((i + 1)). ${tasks[i]}"
    done
  fi
}

# Function to mark a task as completed
complete_task() {
  local task_index=$1
  if [ "$task_index" -ge 1 ] && [ "$task_index" -le "${#tasks[@]}" ]; then
    local completed_task="${tasks[$((task_index - 1))]}"
    tasks[$((task_index - 1))]="[Completed] $completed_task"
    echo "Task marked as completed: $completed_task"
  else
    echo "Invalid task index. Please provide a valid task number."
  fi
}

# Function to delete a task
delete_task() {
  local task_index=$1
  if [ "$task_index" -ge 1 ] && [ "$task_index" -le "${#tasks[@]}" ]; then
    local deleted_task="${tasks[$((task_index - 1))]}"
    unset "tasks[$((task_index - 1))]"
    tasks=("${tasks[@]}")
    echo "Task deleted: $deleted_task"
  else
    echo "Invalid task index. Please provide a valid task number."
  fi
}

# Main script starts here
echo "Todo List - Basic Task Manager"

while true; do
  echo ""
  echo "Menu:"
  echo "1. Add a task"
  echo "2. View tasks"
  echo "3. Mark task as completed"
  echo "4. Delete a task"
  echo "5. Exit"
  read -p "Please choose an option (1/2/3/4/5): " choice

  case $choice in
    1)
      read -p "Enter the task: " new_task
      add_task "$new_task"
      ;;
    2)
      view_tasks
      ;;
    3)
      read -p "Enter the task number to mark as completed: " task_number
      complete_task "$task_number"
      ;;
    4)
      read -p "Enter the task number to delete: " task_number
      delete_task "$task_number"
      ;;
    5)
      echo "Exiting. Goodbye!"
      exit 0
      ;;
    *)
      echo "Invalid choice. Please select a valid option (1/2/3/4/5)."
      ;;
  esac
done
