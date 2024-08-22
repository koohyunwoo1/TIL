// 인덱스드 액세스 타입

// 객체
type PostList = {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}[];

function printAuthorInfo(author: PostList[number]["author"]) {
  console.log(`${author.name} - ${author.id}`);
}

// 객체를 갖는 변수
const post: PostList[number] = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "이천원",
    age: 27,
  },
};

type Tup = [number, string, boolean];

type Tup0 = Tup[0];
type Tup1 = Tup[1];
type Tup2 = Tup[2];
// type Tup3 = Tup[3];

type TupNum = Tup[number];
// 인덱스로 접근하기 때문에 number타입 ㅇㅈ
