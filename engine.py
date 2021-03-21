import argparse
import os
import sys
import importlib.util
import json 

class GameEngine:
    def __init__(self, algo1_path, algo2_path, config):
        
        #importowanie modulow z konkretnej lokalizacji
        spec = importlib.util.spec_from_file_location("algo_strategy", algo1_path)
        algo_strat1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(algo_strat1)

        spec = importlib.util.spec_from_file_location("algo_strategy", algo2_path)
        algo_strat2 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(algo_strat2)

        # z tego mozna wywolywac wszystkie funkcje algo_strategy np. on_turn() itd
        self.algo1 = algo_strat1.AlgoStrategy()
        self.algo2 = algo_strat2.AlgoStrategy()
        with open(config) as json_file:
            self.config = json.load(json_file)

        #przykład
        #self.algo1.on_game_start(self.config)



if __name__ == '__main__':
    
    is_windows = sys.platform.startswith('win')

    parser = argparse.ArgumentParser(description='Run game between 2 algos')
    parser.add_argument('algo1', help='First algo name')
    parser.add_argument('algo2', help='Second algo name')
    parser.add_argument('config', help='Name of config file')
    args = parser.parse_args()

    algo1 = args.algo1
    algo2 = args.algo2
    config = args.config

    

    file_dir = os.path.dirname(os.path.realpath(__file__))

    strategy_path1 = file_dir + "\\" + algo1 + "\\algo_strategy.py" if is_windows \
        else file_dir + "/" + algo1 + "/algo_strategy.py" 
    strategy_path2 = file_dir + "\\" + algo2 + "\\algo_strategy.py" if is_windows \
        else file_dir + "/" + algo2 + "/algo_strategy.py" 
    config_path = file_dir + "\\" + config if is_windows else file_dir + "/" + config 
    
    # zeby dalo sie gamelib zaimportowac
    gamelib_path1 = file_dir + "\\" + algo1  if is_windows else file_dir + "/" + algo1  
    sys.path.insert(1, gamelib_path1)
    gamelib_path2 = file_dir + "\\" + algo2  if is_windows else file_dir + "/" + algo2  
    sys.path.insert(1, gamelib_path2)


    game_engine = GameEngine(strategy_path1, strategy_path2, config_path)
