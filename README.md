## ⚙️ Setup and Running Instructions

Cloning this project:
```bash
git clone https://github.com/YOUR_USERNAME/In-Memory-DB
```
Replace YOUR_USERNAME with your github username

Navigate to the repository directory:
```bash
cd Data-Processing-and-Storage
```

Ensure you have Python installed:
```bash
Python --version
```
If not download from https://www.python.org/downloads/

Finally run the program from your IDE or in the command line using:
```bash
python main.py
```


Modifications to become official assignment:

One of the more immediate clarifications would be to specfiy whether get(key) should return staged/uncommited values or only the committed ones, to standardize ambiguous behavior. I think that a brief explanation of necesary database concepts would be a helpful inclusion to support the learning of students who are unfamiliar. A more effective way to grade might be to have an automated testing process, or test suite with certain languages given, to test the outputs of the different simple functions. 
This would help to minimize the time that a grader would have to spend with each assignment while also helping students gain exposure to 
adhering to industry unit testing standards and practices.