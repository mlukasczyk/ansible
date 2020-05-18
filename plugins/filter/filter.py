#!/usr/bin/env python3
class FilterModule:
    
    @staticmethod
    def filters():
        return {
            'split_at_newline': FilterModule.split_at_newline,
            'diff': FilterModule.diff
        }
    
    @staticmethod
    def split_at_newline(text):
        return text.splitlines()


    @staticmethod
    def diff(int_list, run_list):
        return_list = []
        new_dict = {}
        int_set_list = set(int_list)
        run_set_list = set(run_list)

        #Perform set "diff' operation
        new_dict.update({'add': list(int_set_list - run_set_list)})
        new_dict.update({'del': list(run_set_list - int_set_list)})
        
        return_list.append(new_dict)
    
        return return_list
