#!pip install deepface
from deepface import DeepFace

models = ['VGG-Face', 'Facenet', 'OpenFace', 'DeepFace'
           , 'DeepID', 'Dlib', 'ArcFace',"Facenet512","SFace"]
metrics = ['cosine', 'euclidean', 'euclidean_l2']
obj = DeepFace.verify("shivam-now.jpeg", "shivam_old.jpeg"
   , model_name = models[0], distance_metric = metrics[0])
print(obj)

#obj2=DeepFace.analyze(img_path = "raj_2.png", actions = #['age', 'gender', 'race', 'emotion'])
#print(obj2)
