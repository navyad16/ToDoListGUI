import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidgetItem, QCheckBox, QMessageBox
)
from PyQt5.QtCore import Qt
from ToDo_ui import Ui_Form
from ToDo_DB import fetch_tasks, add_task, delete_task, update_status

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.load_tasks()

        self.ui.btnAdd.clicked.connect(self.add_task)
        self.ui.btnDelete.clicked.connect(self.delete_selected_task)

    def load_tasks(self):
        self.ui.tableTasks.setRowCount(0)
        tasks = fetch_tasks()
        self.ui.tableTasks.setRowCount(len(tasks))
        self.ui.tableTasks.setHorizontalHeaderLabels(['Task', 'Completed'])

        for row, (task_id, title, is_done) in enumerate(tasks):
            # Task title
            title_item = QTableWidgetItem(title)
            title_item.setData(Qt.UserRole, task_id)
            self.ui.tableTasks.setItem(row, 0, title_item)

            # Completed checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(is_done)
            checkbox.stateChanged.connect(
                lambda state, tid=task_id: update_status(tid, state == Qt.Checked)
            )
            self.ui.tableTasks.setCellWidget(row, 1, checkbox)

    def add_task(self):
        title = self.ui.lineEditTask.text().strip()
        if title:
            add_task(title)
            self.ui.lineEditTask.clear()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Input Error", "Task title cannot be empty.")

    def delete_selected_task(self):
        row = self.ui.tableTasks.currentRow()
        if row >= 0:
            item = self.ui.tableTasks.item(row, 0)
            task_id = item.data(Qt.UserRole)
            delete_task(task_id)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())

