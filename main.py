
def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }def count_batteries_by_health(present_capacities):
    
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    
    for capacity in present_capacities:
       
        rated_capacity = 120 
        soh = (capacity / rated_capacity) * 100

        
        if soh > 80:
            healthy_count += 1
        elif soh >= 62:
            exchange_count += 1
        else:
            failed_count += 1

   
    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }



def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
