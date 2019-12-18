#!/usr/bin/env python3

import argparse
import pandas as pd


def main():
   argsparser = argparse.ArgumentParser()
   argsparser.add_argument('dataset_name')
   argsparser.add_argument('input_file')
   argsparser.add_argument('output_file')
   args = argsparser.parse_args()

   df_in = pd.read_csv(args.input_file)
   df_out = df_in[df_in.dataset == args.dataset_name]

   df_out.to_csv(args.output_file, index=False)


if __name__ == '__main__':
   main()

