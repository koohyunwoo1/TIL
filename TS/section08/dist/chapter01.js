// 인덱스드 액세스 타입
function printAuthorInfo(author) {
    console.log(`${author.name} - ${author.id}`);
}
// 객체를 갖는 변수
const post = {
    title: "게시글 제목",
    content: "게시글 본문",
    author: {
        id: 1,
        name: "이천원",
        age: 27,
    },
};
export {};
// 인덱스로 접근하기 때문에 number타입 ㅇㅈ
