_base_ = [
    '../../../_base_/datasets/nway_kshot/few_shot_voc_ms.py',
    '../../../_base_/schedules/schedule.py', '../../vfa_r101_c4.py',
    '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        save_dataset=True,
        dataset=dict(
            type='FewShotVOCDefaultDataset',
            ann_cfg=[dict(method='MetaRCNN', setting='SPLIT1_1SHOT')],
            num_novel_shots=1,
            num_base_shots=1,
            classes='ALL_CLASSES',
        )),
    val=dict(classes='ALL_CLASSES'),
    test=dict(classes='ALL_CLASSES'),
    model_init=dict(classes='ALL_CLASSES'))
evaluation = dict(
    interval=400, class_splits=['BASE_CLASSES', 'NOVEL_CLASSES'])
checkpoint_config = dict(interval=400)
optimizer = dict(lr=0.001)
lr_config = dict(warmup=None)
runner = dict(max_iters=400)
load_from = 'work_dirs/vfa_r101_c4_8xb4_voc-split1_base-training/iter_18000.pth'

# model settings
model = dict(frozen_parameters=[
    'backbone', 'shared_head',  'aggregation_layer',  'rpn_head',
])