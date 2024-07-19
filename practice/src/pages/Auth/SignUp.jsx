import React, { useState} from "react";
import "../../styles/Auth/SignUp.css";
import LogOutHeader from "../../components/Home/LogOutHeader";


const SignUp = () => {

  const [form, setForm] = useState({
    email: "",
    nickname: "",
    password: "",
    confirmPassword: "",
    weight: "",
    region: "",
  })

  const [ errors, setErrors ] = useState({})
  
  const handleChange = (e) => {
    const { name, value } = e.target
    setForm({
      ...form,
      [name]:value,
    })
  }

  const validate = () => {
    const errors = {}
    if (!form.nickname) errors.nickname = "닉네임은 필수입니다."
    if (!form.email) errors.email = "이메일은 필수입니다."
    if (!/\S+@\S+\.\S+/.test(form.email)) errors.email = "이메일이 유효하지 않습니다"
    if (!form.password) errors.password = "비밀번호는 필수입니다."
    if (!form.password.length < 8) errors.password = "비밀번호는 최소 8자리 입니다."
    if (form.password !== form.confirmPassword) errors.confirmPassword = "비밀번호가 일치하지 않습니다."
    if (!form.weight) errors.weight = "체중은 필수입니다."
    return errors
  }
  
  const handleSubmit = (e) => {
    e.preventDefault()
    const validationErrors = validate()
    setErrors(validationErrors)

    if (Object.keys(validationErrors).length === 0) {
      console.log("Form submitted", form)
      // 회원 가입 로직 처리
    }
  }
  return (
    <div>
      <LogOutHeader />
      <form onSubmit={handleSubmit} className="SignUp">
        <h1>회원 가입</h1>
        <div>
          <label>이메일</label>
          <input type="email" name="email" value={form.email} onChange={handleChange} />
          {errors.email && <p>{errors.email}</p>}
        </div>
        <div>
          <label>닉네임</label>
          <input type="text" name="nickname" value={form.nickname} onChange={handleChange} />
          {errors.nickname && <p>{errors.nickname}</p>}
        </div>
        <div>
          <label>비밀번호</label>
          <input type="password" name="password" value={form.password} onChange={handleChange} />
          {errors.password && <p>{errors.password}</p>}
        </div>
        <div>
          <label>비밀번호 확인</label>
          <input type="password" name="confirmPassword" value={form.confirmPassword} onChange={handleChange} />
          {errors.confirmPassword && <p>{errors.confirmPassword}</p>}
        </div>
        <div>
          <label>체중</label>
          <input type="number" name="weight" value={form.weight} onChange={handleChange} />
          {errors.weight && <p>{errors.weight}</p>}
        </div>
        <div>
          <label>사는 지역</label>
          <input type="text" name="region" value={form.region} onChange={handleChange} />
          {errors.region && <p>{errors.region}</p>}
        </div>
        <button type="submit">회원 가입</button>
      </form>
    </div>
  );
};

export default SignUp;
