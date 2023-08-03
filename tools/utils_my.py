import json
import csv



class file_process(object):
    def __str__(self) -> str:
        return "该函数主要对文件进行操作，例如打开/保存文件等"

    def read_json_dumps(self, path):
        with open(path, 'r', encoding='utf-8') as fr:
            data = [json.loads(l) for l in fr]
        return data
    
    def read_json_dump(self, path):
        with open(path, 'r', encoding='utf-8') as fr:
            data = json.load(fr)
        return data
    
    def read_csv(self, path):
        with open(path, 'r', encoding='utf-8') as fr:
            reader = csv.reader(fr)
            data = [l for l in reader]
        return data

    def write_json_dumps(self, path, data):
        with open(path, mode="w", encoding="utf8") as fw:
            for line in data:
                fw.write(json.dumps(line, ensure_ascii=False))
                fw.write("\n")
                
    def write_data_common(sllf, path, data):
        with open(path, 'w', encoding='utf-8') as fw:
            fw.writelines(data)

    def write_csv(sllf, path, data):
        with open(path, 'w', encoding='utf-8') as fw:
            writer = csv.writer(fw)
            writer.writerows(data)
