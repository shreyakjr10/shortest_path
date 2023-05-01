import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
G = nx.Graph()
G.add_node("Delhi")
G.add_node("Mumbai")
G.add_node("Bangalore")
G.add_node("Kolkata")
G.add_node("Hyderabad")
G.add_node("Chennai")
G.add_node("Jaipur")
G.add_node("Lucknow")
G.add_node("Ahmedabad")
G.add_node("Pune")
G.add_node("Surat")
G.add_edge("Delhi", "Mumbai", weight=4.5)
G.add_edge("Delhi", "Bangalore", weight=6.5)
G.add_edge("Delhi", "Kolkata", weight=4.9)
G.add_edge("Delhi", "Hyderabad", weight=4.9)
G.add_edge("Mumbai", "Bangalore", weight=3.2)
G.add_edge("Mumbai", "Kolkata", weight=5.7)
G.add_edge("Mumbai", "Hyderabad", weight=2.3)
G.add_edge("Bangalore", "Kolkata", weight=5.6)
G.add_edge("Bangalore", "Hyderabad", weight=1.8)
G.add_edge("Bangalore", "Chennai", weight=1)
G.add_edge("Kolkata", "Hyderabad", weight=4.2)
G.add_edge("Kolkata", "Chennai", weight=4.8)
G.add_edge("Hyderabad", "Chennai", weight=1.9)
G.add_edge("Hyderabad", "Jaipur", weight=4.2)
G.add_edge("Hyderabad", "Lucknow", weight=4.1)
G.add_edge("Hyderabad", "Ahmedabad", weight=1.9)
G.add_edge("Jaipur", "Lucknow", weight=1.8)
G.add_edge("Lucknow", "Ahmedabad", weight=3.3)
G.add_edge("Lucknow", "Pune", weight=4)
G.add_edge("Ahmedabad", "Pune", weight=2)
G.add_edge("Ahmedabad", "Surat", weight=0.4)
G.add_edge("Pune", "Surat", weight=1.3)
pos = {
"Delhi": (28.632429, 77.218788),
"Mumbai": (19.075983, 72.877655),
"Bangalore": (12.971599,77.594566),
"Kolkata": (22.5726,88.3639),
"Hyderabad": (17.3850,78.4867),
"Chennai": (13.0827,80.2707),
"Jaipur": (26.9124, 75.7873),
"Lucknow": (26.8467, 80.9462),
"Ahmedabad": (23.0225, 72.5714),
"Pune": (18.5204, 73.8567),
"Surat": (21.1702, 72.8311)
}
def get_route():
    global start
    start = start_entry.get()
    global end
    end = end_entry.get()
    try:
        route = nx.shortest_path(G, source=start, target=end, weight='weight')
        route_label.config(text="Route: " + " -> ".join(route))
    except nx.NetworkXNoPath:
        route_label.config(text="No path found")
root = tk.Tk()
root.title("Indian Capital Cities Route Finder")
root.configure(bg='lightblue')
frame = tk.Frame(root, bg='lightblue')
frame.pack(pady=20)
start_label = tk.Label(frame, text="Starting location:", font=("TkDefaultFont", 12), bg='lightblue')
start_label.grid(row=10, column=0, padx=10)
start_entry = tk.Entry(frame, font=("TkDefaultFont", 12), bg='white')
start_entry.grid(row=10, column=1, padx=10)
end_label = tk.Label(frame, text="Ending location:", font=("TkDefaultFont", 12), bg='lightblue')
end_label.grid(row=11, column=0, padx=10)
end_entry = tk.Entry(frame, font=("TkDefaultFont", 12), bg='white')
end_entry.grid(row=11, column=1, padx=10)
find_route_button = tk.Button(frame, text="Find best route", command=get_route,
font=("TkDefaultFont", 14), bg='blue', fg='white')
find_route_button.grid(row=12, column=0, columnspan=2, pady=20)
route_label = tk.Label(frame, text="", font=("TkDefaultFont", 12), bg='lightblue')
route_label.grid(row=13, column=0, columnspan=2, pady=20)
"""img = ImageTk.PhotoImage(Image.open("maplogo.jpg")) 
label = Label(frame, image = img) 
label.pack()"""
root.mainloop()
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# Determining the shortest path between two cities based on cost
shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')
# Drawing the edges of the shortest path in red color
edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
red_edges = nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2.0)
plt.show()
# Determining the shortest path between two cities based on cost
shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')
cost = nx.shortest_path_length(G, source=start, target=end, weight='weight')
# Printing the result
print("The shortest path between {} and {} is: {}".format(start_entry, end_entry, shortest_path))
print(f"The cost of the shortest path is: {cost*1500}")
