import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
  primes = []
  for number in numbers:
    if is_prime(number):
      primes.append(number)
  return primes

def find_primes_in_range(numbers, chunk_size):
    # Split numbers into chunks
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Create a process pool
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the check_prime_chunk function to each chunk
        results = pool.map(check_prime_chunk, chunks)
    
    # Flatten the results
    primes = [prime for prime_list in results for prime in prime_list]
    return primes

