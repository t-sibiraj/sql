def sql_table_to_md_table(sql_table):
    """Used to convert SQL Table to Markdown Table
        +------+             |------|
        | year |             | year |
        +------+             |------|
        | 2004 |    ---->    | 2004 |
        | 2003 |             | 2003 |
        | 2002 |             | 2002 |
        +------+             |------|

"""
    sql_table = sql_table.strip()
    sql_table = sql_table.split('\n')
    for line in sql_table:
        if '+' in line:
            sql_table[sql_table.index(line)] = line.replace('+','|')
    for line in sql_table:
        print(line.strip())
    
