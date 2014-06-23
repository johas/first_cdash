#include <stdio.h>
#include <math.h>
//#include "mysqrt.h"

double mysqrt(double x)
{
  // if we have both log and exp then use them
#if defined (HAVE_LOG) && defined (HAVE_EXP)
  result = exp(log(x)*0.5);
  fprintf(stdout,"both defined.\n");
#else // otherwise use an iterative approach
  fprintf(stdout,"Not defined.\n");
  return pow(x,0.5);
#endif
}
