# Count the number of solved problems in the playground repository
import glob
from pathlib import Path

path = 'playground/src/main/java/boj/P*.java'

problems = glob.glob(path)
numbers = sorted(int(Path(problem).stem.lstrip('P')) for problem in problems)

content = f'''# test-submodule
    
playground에 등록한 백준 문제는 몇 개일까?
- Java로 푼 문제: {len(numbers)}개

---

{"\n".join(f'- {number}' for number in numbers)}'''

with open('README.md', 'w') as readme:
    readme.write(content)
