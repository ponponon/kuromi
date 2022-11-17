# 项目描述

短视频入库和查询

# 项目部署

克隆项目

```shell
git clone http://120.26.52.123:8081/zj_bqjc/svddb_cli.git/
```

## 构建本地开发环境

### 安装开发环境

```shell
pipenv install --python=python3.9
```

### 启动虚拟环境

```shell
pipenv shell
```

### 安装第三方依赖

必须的依赖

```shell
pip install -r nec-requirements.txt
```

辅助依赖

```shell
pip install -r dev-requirements.txt
```

# 用户使用

## 入库

```shell
python sdk.py ingest --file_path ./media/322da6a8-4528-11ec-bc7d-ca46a7d39475-v4_t11-vlo0D3AxeS.mp4
```

## 查询

```shell
python sdk.py search --file_path ./media/322da6a8-4528-11ec-bc7d-ca46a7d39475-v4_t11-vlo0D3AxeS.mp4
```

# 常见 QA：

## Q: milvus 的 FLOAT_VECTOR 是 4 字节 还是 8 字节？

A: 4 字节的
参考：[Prepare Schema](https://milvus.io/cn/docs/v2.0.x/create_collection.md#Prepare-Schema)

## 拆帧获取到的帧（frame），单个需要占用多少的内存









```shell
python sdk.py create-single --video_file_path /home/pon/Downloads/svddb/sample/video/10.mp4 --output_dir_path /home/pon/code/vobile/svddb_cli/resource/dna
```


# 母本生成

```shell
nohup python sdk.py create-batch --video_file_path /home/pon/Downloads/svddb/meta/video/ --output_dir_path /home/pon/Downloads/svddb/meta/dna --meta true > run_meta.log 2>&1 &
```


# 样本生成

```shell
nohup python sdk.py create-batch --video_file_path /home/pon/Downloads/guihuayuan/s5 --output_dir_path /home/pon/Downloads/guihuayuan/s5-dna --meta true > run_sample-guihuayuan.log 2>&1 &
```





```shell
nohup python sdk.py create-batch --video_file_path /home/vobile/disk/规划院2022-11-12/sample/negative/easy --output_dir_path /home/vobile/disk/规划院2022-11-12/sample/negative/easy-dna > run_sample.log 2>&1 &
```


```shell
nohup python sdk.py create-batch --video_file_path /home/vobile/disk/规划院2022-11-12/sample/negative/hard --output_dir_path /home/vobile/disk/规划院2022-11-12/sample/negative/hard-dna > run_sample-hard-dna.log 2>&1 &
```

```shell
nohup python sdk.py create-batch --video_file_path /home/vobile/disk/规划院2022-11-12/sample/negative/middle --output_dir_path /home/vobile/disk/规划院2022-11-12/sample/negative/middle-dna > run_sample-middle-dna.log 2>&1 &
```








```shell
nohup python sdk.py create-batch --video_file_path /home/vobile/disk/规划院2022-11-12/sample/positive/changjing16_shuping_butong --output_dir_path /home/vobile/disk/规划院2022-11-12/sample/positive/changjing16_shuping_butong-dna > run_sample-changjing16_shuping_butong-dna.log 2>&1 &
```


```shell
nohup python sdk.py create-batch --video_file_path /home/vobile/disk/规划院2022-11-12/extract --output_dir_path /home/vobile/disk/规划院2022-11-12/extract-dna > run_sample-extract-dna.log 2>&1 &
```




nohup python sdk.py  init-dna --src_dir /home/vobile/disk/规划院2022-11-12/extract > run_sample-extract-dna.log 2>&1 &


nohup python sdk.py  init-dna --src_dir /home/vobile/disk/规划院2022-11-12/extract > run_sample-extract-dna.log 2>&1 &




nohup  python sdk.py  init-dna --src_dir /home/vobile/disk/规划院2022-11-12/sample-bak > run_sample.log 2>&1 &