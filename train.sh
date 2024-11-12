# pip install yapf==0.40.1
# CUDA_VISIBLE_DEVICES=0 python train.py configs/vfa/voc/vfa_split1/vfa_r101_c4_8xb4_voc-split1_base-training.py
# CUDA_VISIBLE_DEVICES=0 python train.py configs/vfa/coco/vfa_r101_c4_8xb4_coco_base-training.py
CUDA_VISIBLE_DEVICES=0 python train_att.py configs/vfa/attribution/1shot_fine_tuning.py
# CUDA_VISIBLE_DEVICES=0 python train_att.py configs/vfa/attribution/base_training.py