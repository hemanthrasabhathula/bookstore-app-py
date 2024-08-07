from app.models.branch import Branch


def get_branches():
    return Branch.get_all_branches()


def get_branch_by_id(branch_id):
    return Branch.get_branch_by_id(branch_id)


def insert_branch(branch):
    return Branch.add_branch(branch)


def del_branch_by_id(branch_id):
    return Branch.del_branch_by_id(branch_id)
