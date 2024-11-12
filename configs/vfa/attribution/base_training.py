_base_ = [
    '../../../_base_/datasets/nway_kshot/base_attribution_ms.py',
    '../../../_base_/schedules/schedule.py', '../../vfa_r101_c4.py',
    '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotAttributionDataset
# FewShotAttributionDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        save_dataset=False,
        dataset=dict(classes='BASE_CLASSES'),
        support_dataset=dict(classes='BASE_CLASSES')),
    val=dict(classes='BASE_CLASSES'),
    test=dict(classes='BASE_CLASSES'),
    model_init=dict(classes='BASE_CLASSES'))
lr_config = dict(warmup_iters=10, step=[2000, 2500])
evaluation = dict(interval=1000)
checkpoint_config = dict(interval=1000)
runner = dict(max_iters=3000)
optimizer = dict(lr=0.02)
# model settings
model = dict(roi_head=dict(bbox_head=dict(num_classes=15, num_meta_classes=15)))