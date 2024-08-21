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

function printAuthorInfo(author: Post["author"]) {
  console.log(`${author.name} - ${author.id}`);
}

// 객체를 갖는 변수
const post: Post = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "이천원",
    age: 27,
  },
};
