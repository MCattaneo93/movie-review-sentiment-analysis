#pre-process

A python script which takes input files with plain text; cleans, tokenizes, and vectorizes the plaintext, with some label (0 or 1).

Input must match the following:
Be placed in the same directory as the script
In a folder labeled, train and test
Both folders have a folder labeled pos and neg

From there the script will read each text file.  

How to run:
From Terminal:
1)	python pre-process.py
2)	python pre-process.py vocab_file.txt train_data_folder_path test_data_folder_path
3)	python pre-process.py FEATURE_LENGTH

#LR

A python script which contains the class LogisticRegression, a logistic regression classifier which predicts if a movie review is positive or negative. 

Input must match the following:
Be placed in the same directory as the script
If not passing an argument, must be called "train_data.txt" and "test_data.txt"
Parameters must be stored in a file called, movie-review-BOW.LR

How to run:
From Terminal:
1)	python LR.py
2) python LR.py debug
3) python LR.py unsup train_file_name.txt test_file_name.txt
4) python LR.py test_data.txt
5) python LR.py train_file_name.txt test_file_name.txt

Option 1, handles the parameters, and stores them to the movie-review-BOW.LR file accordingly. Automatically runs on the default file information from pre-process.py

Option 2, has the test data which is incorrectly labeled printed to an EXCEL worksheet, separated by False Positives and False Negatives

Option 3, provides predictions to data which does not have a label

For example, if you want to run on the small example given in the pdf, you would use python LR.py unsup train_file_name.txt test_file_name.txt, and it would give a prediction. 

#loop_script

If interested, I've included the looping script, which iterates over various values of eta and feature length, in order to determine what the best combination is, with the current feature selection

Run from terminal:
python loop_script.py
