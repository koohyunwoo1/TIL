### js로 되어있는 파일 ts로 바꾸는 방법

1 . 타입선언

- npm i @types/node @types/react @types/react-dom @types/jest

2. tsconfig.json

```
{
  "compilerOptions": {
    "target": "ES5",
    "module": "CommonJS",
    "strict": true,
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}

```

3. 모든 js -> JSX

4. 개별 하나씩 TSX
