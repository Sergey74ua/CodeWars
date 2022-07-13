#Grasshopper - Check for factor

function CheckForFactor([int] $base, [int] $factor) {
  if ($base % $factor) {
    return $false
  }
  return $true
}