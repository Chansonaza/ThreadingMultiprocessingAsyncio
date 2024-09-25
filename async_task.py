import asyncio

async def async_write_to_file(filename, data, duration):
    await asyncio.sleep(duration)
    try:
        with open(filename, 'w') as file:
            file.write("\n".join(map(str, data)))
        print(f"Finished writing to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")


async def run_async_tasks():
    data = [2,3,5,7]
    await asyncio.gather(
        async_write_to_file("primes.txt", data, 2),
        async_write_to_file("primes2.txt", data, 4)
    )

