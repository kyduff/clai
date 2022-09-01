import argparse
from metric import metric_utils

def get_parser():
  parser = argparse.ArgumentParser()

  parser.add_argument('-preds', type=str, required=True)
  parser.add_argument('-golds', type=str, required=True)
  parser.add_argument('-verbose', action='store_true')

  return parser


def main(opt):
  golds = opt.golds
  preds = opt.preds

  with open(golds, 'r') as g, open(preds, 'r') as p:
    gs = [l.strip() for l in g]
    ps = [l.strip() for l in p]

  total = 0
  for pred, gold in zip(ps, gs):
    score = metric_utils.compute_metric(pred, 1.0, gold)
    total += score

    if opt.verbose:
      print(f'pred: {pred}')
      print(f'gold: {gold}')
      print(f'score: {score}')
      print()

  print(f'{total/len(ps)}')

if __name__ == "__main__":
  parser = get_parser()
  opt = parser.parse_args()

  main(opt)

