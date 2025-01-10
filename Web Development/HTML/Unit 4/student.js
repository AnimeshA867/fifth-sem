class Student {
  static students = [];

  constructor(id, name, address, email) {
    this.id = id;
    this.name = name;
    this.address = address;
    this.email = email;
    Student.students.push({ id, name, address, email });
  }

  static addStudent() {
    const id = prompt("Enter the student's id");
    const name = prompt("Enter the student's name");
    const address = prompt("Enter the student's address");
    const email = prompt("Enter the student's email");
    new Student(id, name, address, email);
  }

  static showStudents() {
    console.log("Reached here.");
    let div = "";
    for (let student of Student.students) {
      div += `<ul>
        <li>Name: ${student.name}</li>
        <li>Address: ${student.address}</li>
        <li>Email: ${student.email}</li>
      </ul>
      `;
    }
    const newDiv = document.getElementById("div");
    newDiv.innerHTML = div;
  }
}

// Example usage:
const add = () => {
  console.log("This is working.");
  Student.addStudent();
};

// Adding a student and displaying the list
// add();
Student.showStudents();
