'''
Created on 2012-6-26

@author: yunify
'''
'''
    Here are constants use in cli tools
'''

# actions definition
# images
ACTION_DESCRIBE_IMAGES = "DescribeImages"
ACTION_CAPTURE_INSTANCE = "CaptureInstance"
ACTION_DELETE_IMAGES = "DeleteImages"
ACTION_MODIFY_IMAGE_ATTRIBUTES = "ModifyImageAttributes"
# instances
ACTION_DESCRIBE_INSTANCES = "DescribeInstances"
ACTION_RUN_INSTANCES = "RunInstances"
ACTION_TERMINATE_INSTANCES = "TerminateInstances"
ACTION_START_INSTANCES = "StartInstances"
ACTION_RESTART_INSTANCES = "RestartInstances"
ACTION_STOP_INSTANCES = "StopInstances"
ACTION_RESIZE_INSTANCES = "ResizeInstances"
ACTION_RESET_INSTANCES = "ResetInstances"
ACTION_MODIFY_INSTANCE_ATTRIBUTES = "ModifyInstanceAttributes"
# volumes
ACTION_DESCRIBE_VOLUMES = "DescribeVolumes"
ACTION_CREATE_VOLUMES = "CreateVolumes"
ACTION_DELETE_VOLUMES = "DeleteVolumes"
ACTION_ATTACH_VOLUMES = "AttachVolumes"
ACTION_DETACH_VOLUMES = "DetachVolumes"
ACTION_RESIZE_VOLUMES = "ResizeVolumes"
ACTION_MODIFY_VOLUME_ATTRIBUTES = "ModifyVolumeAttributes"
# key pair
ACTION_DESCRIBE_KEY_PAIRS = "DescribeKeyPairs"
ACTION_CREATE_KEY_PAIR = "CreateKeyPair"
ACTION_DELETE_KEY_PAIRS = "DeleteKeyPairs"
ACTION_ATTACH_KEY_PAIRS = "AttachKeyPairs"
ACTION_DETACH_KEY_PAIRS = "DetachKeyPairs"
ACTION_MODIFY_KEYPAIR_ATTRIBUTES = "ModifyKeyPairAttributes"
# security group
ACTION_DESCRIBE_SECURITY_GROUPS = "DescribeSecurityGroups"
ACTION_CREATE_SECURITY_GROUP = "CreateSecurityGroup"
ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES = "ModifySecurityGroupAttributes"
ACTION_APPLY_SECURITY_GROUP = "ApplySecurityGroup"
ACTION_DELETE_SECURITY_GROUPS = "DeleteSecurityGroups"
ACTION_DESCRIBE_SECURITY_GROUP_RULES = "DescribeSecurityGroupRules"
ACTION_ADD_SECURITY_GROUP_RULES = "AddSecurityGroupRules"
ACTION_DELETE_SECURITY_GROUP_RULES = "DeleteSecurityGroupRules"
ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES = "ModifySecurityGroupRuleAttributes"
# vxnets
ACTION_DESCRIBE_VXNETS = "DescribeVxnets"
ACTION_CREATE_VXNETS = "CreateVxnets"
ACTION_DELETE_VXNETS = "DeleteVxnets"
ACTION_JOIN_VXNET = "JoinVxnet"
ACTION_LEAVE_VXNET = "LeaveVxnet"
ACTION_MODIFY_VXNET_ATTRIBUTES = "ModifyVxnetAttributes"
ACTION_DESCRIBE_VXNET_INSTANCES = "DescribeVxnetInstances"
# router
ACTION_CREATE_ROUTERS = "CreateRouters"
ACTION_UPDATE_ROUTERS = "UpdateRouters"
ACTION_DELETE_ROUTERS = "DeleteRouters"
ACTION_JOIN_ROUTER = "JoinRouter"
ACTION_LEAVE_ROUTER = "LeaveRouter"
ACTION_POWEROFF_ROUTERS = "PowerOffRouters"
ACTION_POWERON_ROUTERS = "PowerOnRouters"
ACTION_DESCRIBE_ROUTERS = "DescribeRouters"
ACTION_DESCRIBE_ROUTER_VXNETS = "DescribeRouterVxnets"
ACTION_MODIFY_ROUTER_ATTRIBUTES = "ModifyRouterAttributes"
ACTION_DESCRIBE_ROUTER_STATICS = "DescribeRouterStatics"
ACTION_ADD_ROUTER_STATICS = "AddRouterStatics"
ACTION_DELETE_ROUTER_STATICS = "DeleteRouterStatics"
# eip
ACTION_ASSOCIATE_EIP = "AssociateEip"
ACTION_DISSOCIATE_EIPS = "DissociateEips"
ACTION_ALLOCATE_EIPS = "AllocateEips"
ACTION_RELEASE_EIPS = "ReleaseEips"
ACTION_DESCRIBE_EIPS = "DescribeEips"
ACTION_MODIFY_EIP_ATTRIBUTES = "ModifyEipAttributes"
ACTION_CHANGE_EIPS_BANDWIDTH = "ChangeEipsBandwidth"
