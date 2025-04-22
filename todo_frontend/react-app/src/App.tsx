import React, { useEffect, useState } from "react";
import axios from "axios";

type Task = {
  id: number;
  title: string;
  done: boolean;
};

const API_URL = "http://localhost:8000";

const App = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState("");

  const fetchTasks = async () => {
    const res = await axios.get(`${API_URL}/tasks`);
    setTasks(res.data);
  };

  const addTask = async () => {
    if (!newTask.trim()) return;
    await axios.post(`${API_URL}/tasks`, { title: newTask });
    setNewTask("");
    fetchTasks();
  };

  const deleteTask = async (id: number) => {
    await axios.delete(`${API_URL}/tasks/${id}`);
    fetchTasks();
  };

  const toggleDone = async (task: Task) => {
    if (task.done) {
      // ✅ 完了を取り消す
      await axios.delete(`${API_URL}/tasks/${task.id}/done`);
    } else {
      // ✅ 完了にする
      await axios.put(`${API_URL}/tasks/${task.id}/done`);
    }
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>ToDo List</h1>
      <input
        value={newTask}
        onChange={(e) => setNewTask(e.target.value)}
        placeholder="タスクを入力"
      />
      <button onClick={addTask}>追加</button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <label>
              <input
                type="checkbox"
                checked={task.done}
                onChange={() => toggleDone(task)}
              />
              {task.title}
            </label>
            <button onClick={() => deleteTask(task.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
