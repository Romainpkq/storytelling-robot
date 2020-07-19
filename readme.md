# Storytelling robot
## introduction
The project is to realize a storytelling robot, the project is divided to 2 parts.One is to "local" whose the files are in local computer.
The other "serveur" whose files are in the service.
## datasets
 1. "chinese": the json format data that convert from chinese
 1. "chinese_to_english_story": the txt format data that covert from chinese (number: 4658)
 1. "english_short_story": short english story (number: 283)
 1. "french_story": the french story (number: 925)
 1. "merge_chinese_english_short_story": "chinese_to_english_story" + "english_short_story"
## Train
We use files in the "chinese" to fine-tune the 345M gpt-2 model, the detail can see in https://github.com/nshepperd/gpt-2.

## Process
We use the audio system of Windows to tell the story. We run the run.py in local directory to realize the storytelling robot.
if you want to generate story in the service, you just need to run the file "run.py" in the directory "gpt-2/src".
The generated story will be saved in "gpt-2/samples/story_final".

**Attention: You should change the path.**

### pretraining weights
You can the pretraining weights from Baidu cloud.
link：https://pan.baidu.com/s/1eaNYTTPgLn-eLOQ_Z8fkYQ 
password：3bta

After download the weights, uncompress to the "gpt-2/models/345MChinese" directory.
