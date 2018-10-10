# Kernels

Read about kernels(up to page 8, not throughly, just to get the sense) 

http://www.kernel-machines.org/publications/pdfs/0701907.pdf

Read about KPCA in Bishop 586-590

Some intuition about kernels:

https://sebastianraschka.com/Articles/2014_kernel_pca.html 

https://arxiv.org/pdf/1207.3538.pdf 

For every dataset from list 1, for every algorithm from list 2 and for every kernel from list 3 perform the next steps:

•	Apply dimension reduction to 2-d and visualize classifier decision boundaries using 2 classes only. 

•	Answer the question: which classifier and kernel do you think work best with the given data (for 2 classes)?

•	Calculate accuracy for all classifiers and kernels for all classes, see how it fits your assumption from above answer(use 0.2-0.3 of the data as test, rest as train).
Helpful reference: 

https://www.kaggle.com/jsultan/visualizing-classifier-boundaries-using-kernel-pca/notebook

List 1 – datasets:

•	Mnist (load from sklearn.dataset)

•	Pokemon dataset (with label – is_legendary, preprocess as you wish to get acc>0.9 for all classifiers and kernels) 
https://www.kaggle.com/rounakbanik/pokemon 

List 2 – classification algorithms:

•	Logistic Regression

•	Naïve Bayes

•	KNN

•	Random Forest

•	SVM – Linear

•	SVM – rbf

No need for “SVM – poly”!!!

List 3 – kernels:

•	Linear

•	Rbf

•	Poly

•	Sigmoid

•	Cosine

Tip: generic is key!



  
