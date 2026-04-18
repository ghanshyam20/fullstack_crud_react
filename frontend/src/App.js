import { useEffect, useState } from "react";

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [editId, setEditId] = useState(null);

  const fetchItems = () => {
    fetch("http://127.0.0.1:8000/api/items/")
      .then(res => res.json())
      .then(data => setItems(data));
  };

  useEffect(() => {
    fetchItems();
  }, []);

  const addItem = (e) => {
    e.preventDefault();

    fetch("http://127.0.0.1:8000/api/items/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name })
    })
      .then(res => res.json())
      .then(() => {
        setName("");
        fetchItems();
      });
  };

  const updateItem = (e) => {
    e.preventDefault();

    fetch(`http://127.0.0.1:8000/api/items/update/${editId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name })
    })
      .then(res => res.json())
      .then(() => {
        setName("");
        setEditId(null);
        fetchItems();
      });
  };

  const deleteItem = (id) => {
    fetch(`http://127.0.0.1:8000/api/items/${id}/`, {
      method: "DELETE"
    }).then(() => fetchItems());
  };

  return (
    <div>
      <h1>Items</h1>

      <form onSubmit={editId ? updateItem : addItem}>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter item"
        />
        <button type="submit">
          {editId ? "Update" : "Add"}
        </button>
      </form>

      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}

            <button onClick={() => {
              setEditId(item.id);
              setName(item.name);
            }}>
              Edit
            </button>

            <button onClick={() => deleteItem(item.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;