#!/usr/bin/python3


def pascal_triangle(n):
  """
  Generates Pascal's triangle up to n levels.

    Args:
        n (int): Number of levels in the triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
            Each inner list corresponds to a row in the triangle.
  """
  if n <= 0:
      return []
  triangle = []
  for i in range(n):
      row = []
      for j in range(i+1):
          if j == 0 or j == i:
              row.append(1)
          else:
              row.append(triangle[i-1][j-1] + triangle[i-1][j])
      triangle.append(row)
  return triangle
